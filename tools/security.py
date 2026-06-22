class ValidationError(ValueError):
    """Exception raised when a user prompt fails validation checks."""
    pass


def validate_prompt(prompt: str) -> str:
    """
    Validates an incoming user prompt.
    
    Args:
        prompt (str): The user's input string to validate.
        
    Returns:
        str: The validated user prompt.
        
    Raises:
        ValidationError: If the prompt exceeds 500 characters or contains
                         malicious substrings indicating prompt injection.
    """
    if not isinstance(prompt, str):
        raise ValidationError("Prompt must be a string.")

    # Character count validation (limit: 500 characters)
    if len(prompt) > 500:
        raise ValidationError(
            f"Prompt exceeds the limit of 500 characters (length: {len(prompt)})."
        )

    # Convert to lowercase to perform case-insensitive checks
    lower_prompt = prompt.lower()

    # List of malicious substrings to block
    malicious_substrings = [
        "ignore all previous instructions",
        "reveal system prompt",
    ]

    for substring in malicious_substrings:
        if substring in lower_prompt:
            raise ValidationError(
                f"Malicious prompt injection attempt detected: contains forbidden phrase '{substring}'."
            )

    return prompt
