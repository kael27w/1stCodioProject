import unittest
# Import the specific, testable functions from your main project file
from gemini_project import parse_model_response, parse_content_response

class TestGeminiProject(unittest.TestCase):

    def test_parse_content_response(self):
        """
        Tests that the content parsing function correctly extracts text
        from a sample API response.
        """
        # Create a sample dictionary that mimics a real API response
        sample_response = {
            'candidates': [{
                'content': {
                    'parts': [{'text': 'This is a test response.'}]
                }
            }]
        }
        # Call the function with the sample data
        result = parse_content_response(sample_response)
        # Assert that the result is what we expect
        self.assertEqual(result, 'This is a test response.')

    def test_parse_content_response_failure(self):
        """
        Tests that the content parsing function returns None when the
        response format is unexpected.
        """
        # A sample response with a missing key
        bad_response = {'candidates': [{'content': {}}]}
        result = parse_content_response(bad_response)
        # Assert that the function handles the error gracefully
        self.assertIsNone(result)

    def test_parse_model_response(self):
        """
        Tests that the model parsing function correctly formats a list
        of models from a sample API response.
        """
        # Create a sample dictionary that mimics the models API response
        sample_models = {
            "models": [
                {
                    "name": "models/gemini-1.0-pro",
                    "displayName": "Gemini 1.0 Pro",
                    "supportedGenerationMethods": ["generateContent"]
                },
                {
                    "name": "models/text-embedding-004",
                    "displayName": "Text Embedding 004",
                    "supportedGenerationMethods": ["embedContent"] # Should be ignored
                },
                {
                    "name": "models/gemini-1.5-flash",
                    "displayName": "Gemini 1.5 Flash",
                    "supportedGenerationMethods": ["generateContent"]
                }
            ]
        }
        # The expected output after formatting
        expected_list = [
            "- Gemini 1.0 Pro (models/gemini-1.0-pro)",
            "- Gemini 1.5 Flash (models/gemini-1.5-flash)"
        ]
        # Call the function with the sample data
        result = parse_model_response(sample_models)
        # Assert that the resulting list is identical to our expected list
        self.assertEqual(result, expected_list)

# This block allows the test file to be run directly
if __name__ == '__main__':
    unittest.main()
