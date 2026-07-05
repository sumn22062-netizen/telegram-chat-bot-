import os
from google import genai
from google.genai import types
from pydantic import BaseModel,Field
from typing import Optional
from dotenv import load_dotenv
load_dotenv()
client=genai.Client() ## yah AI se connect hota hai

class MessageAnalysis(BaseModel):
    category: str = Field(description="Must be either 'expense', 'note', or 'other'.")
    amount: Optional[float] = Field(default=None, description="The cost or price of the item if category is expense. Null otherwise.")
    item_name: Optional[str] = Field(default=None, description="What was bought if category is expense (e.g. Pizza, Taxi, Book). Null otherwise.")
    summary: Optional[str] = Field(default=None, description="A clean, concise summary in Hinglish/English of the note if category is note. Null otherwise.")

def analyze_message(text: str) -> MessageAnalysis:
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=text,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=MessageAnalysis,
                system_instruction=(
                    "You are a personal assistant. Analyze the user's message. "
                    "If the user tells you about money they spent, classify it as 'expense' and extract the amount (convert to float) and the item name. "
                    "If the user tells you to remember something, write down a fact, or save a note, classify it as 'note' and summarize it. "
                    "Otherwise (like hi, hello, or random chat), classify it as 'other'."
                )
            ),
        )

        return MessageAnalysis.model_validate_json(response.text)
        
    except Exception as e:
        print(f"Error calling Gemini: {e}")
        # Error aane par safe fallback return karein
        return MessageAnalysis(category="other")
