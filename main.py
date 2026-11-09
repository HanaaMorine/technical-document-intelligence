from app.llm import get_completion

prompt = """
The system must operate below 80°C.
The system must respond within 200 milliseconds.
The system must support 100 simultaneous users.
"""

result = get_completion(prompt)

print(result)