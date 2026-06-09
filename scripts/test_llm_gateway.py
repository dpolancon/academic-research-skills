import unittest
from unittest.mock import patch, MagicMock
import os
import sys
from pathlib import Path

# Ensure scripts folder is on PATH
sys.path.insert(0, str(Path(__file__).resolve().parent))

from llm_gateway import LLMGateway

class TestLLMGateway(unittest.TestCase):
    def setUp(self):
        # Create a simplified mock config
        self.mock_config = {
            "global_settings": {
                "default_provider": "together",
                "default_model": "Qwen/Qwen3.5-9B"
            },
            "providers": {
                "together": {
                    "api_key_env": "TOGETHER_API_KEY",
                    "base_url": "https://api.together.ai/v1"
                },
                "gemini": {
                    "api_key_env": "GEMINI_API_KEY"
                }
            }
        }
        
    @patch("llm_gateway.OpenAI")
    @patch("llm_gateway.genai")
    @patch("builtins.open")
    @patch("yaml.safe_load")
    @patch("pathlib.Path.exists")
    def test_gateway_initialization(self, mock_exists, mock_yaml, mock_open, mock_genai, mock_openai):
        mock_exists.return_value = True
        mock_yaml.return_value = self.mock_config
        
        with patch.dict(os.environ, {"TOGETHER_API_KEY": "fake_together_key", "GEMINI_API_KEY": "fake_gemini_key"}):
            gateway = LLMGateway(config_path="dummy_config.yaml")
            
            # Verify config loading
            self.assertEqual(gateway.config, self.mock_config)
            self.assertEqual(gateway.default_model, "Qwen/Qwen3.5-9B")
            self.assertEqual(gateway.default_provider, "together")
            self.assertEqual(gateway.base_url, "https://api.together.ai/v1")
            
            # Verify client setup
            mock_openai.assert_called_once_with(api_key="fake_together_key", base_url="https://api.together.ai/v1")
            mock_genai.configure.assert_called_once_with(api_key="fake_gemini_key")

    @patch("llm_gateway.OpenAI")
    @patch("llm_gateway.genai")
    @patch("builtins.open")
    @patch("yaml.safe_load")
    @patch("pathlib.Path.exists")
    def test_priority_overrides(self, mock_exists, mock_yaml, mock_open, mock_genai, mock_openai):
        mock_exists.return_value = True
        mock_yaml.return_value = self.mock_config
        
        with patch.dict(os.environ, {"TOGETHER_API_KEY": "fake", "GEMINI_API_KEY": "fake"}):
            # Test constructor argument override (highest priority)
            gateway = LLMGateway(
                config_path="dummy_config.yaml",
                default_model="custom-model-cli",
                default_provider="gemini",
                base_url="https://custom.api.url"
            )
            self.assertEqual(gateway.default_model, "custom-model-cli")
            self.assertEqual(gateway.default_provider, "gemini")
            self.assertEqual(gateway.base_url, "https://custom.api.url")

    @patch("llm_gateway.OpenAI")
    @patch("llm_gateway.genai")
    @patch("builtins.open")
    @patch("yaml.safe_load")
    @patch("pathlib.Path.exists")
    def test_env_var_fallback(self, mock_exists, mock_yaml, mock_open, mock_genai, mock_openai):
        # Test case where config is empty, falls back to env vars
        mock_exists.return_value = False
        
        with patch.dict(os.environ, {
            "TOGETHER_API_KEY": "fake",
            "DEFAULT_MODEL": "env-model",
            "DEFAULT_PROVIDER": "together"
        }):
            gateway = LLMGateway(config_path="non_existent.yaml")
            self.assertEqual(gateway.default_model, "env-model")
            self.assertEqual(gateway.default_provider, "together")

    @patch("llm_gateway.OpenAI")
    @patch("llm_gateway.genai")
    @patch("builtins.open")
    @patch("yaml.safe_load")
    @patch("pathlib.Path.exists")
    def test_tool_mapping_gemini(self, mock_exists, mock_yaml, mock_open, mock_genai, mock_openai):
        mock_exists.return_value = True
        mock_yaml.return_value = self.mock_config
        
        with patch.dict(os.environ, {"TOGETHER_API_KEY": "fake", "GEMINI_API_KEY": "fake"}):
            # Initialize with Gemini as default provider
            gateway = LLMGateway(config_path="dummy_config.yaml", default_provider="gemini", default_model="gemini-1.5-pro")
            
            # OpenAI style tool schema
            openai_tools = [
                {
                    "type": "function",
                    "function": {
                        "name": "search_bibliographic_indexes",
                        "description": "Search indexes",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "query": {"type": "string"}
                            },
                            "required": ["query"]
                        }
                    }
                }
            ]
            
            # Mock Gemini GenerativeModel setup
            mock_model = MagicMock()
            mock_genai.GenerativeModel.return_value = mock_model
            mock_model.start_chat.return_value.send_message.return_value.candidates = []
            
            gateway.generate(
                agent_name="editor_in_chief",
                system_prompt="sys prompt",
                user_prompt="user prompt",
                tools=openai_tools
            )
            
            # Verify GenerativeModel was initialized with correct mapped tools format
            mock_genai.GenerativeModel.assert_called_once()
            called_tools = mock_genai.GenerativeModel.call_args[1]["tools"]
            self.assertEqual(len(called_tools), 1)
            self.assertIn("function_declarations", called_tools[0])
            self.assertEqual(called_tools[0]["function_declarations"][0]["name"], "search_bibliographic_indexes")

if __name__ == "__main__":
    unittest.main()
