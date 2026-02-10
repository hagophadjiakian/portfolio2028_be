from pydantic import BaseModel, EmailStr, Field


class ContactForm(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    subject: str = Field(..., min_length=5, max_length=200)
    message: str = Field(..., min_length=10, max_length=5000)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john@example.com",
                "subject": "Project Inquiry",
                "message": "Hi Hagop, I'm interested in discussing a project."
            }
        }


class ContactResponse(BaseModel):
    success: bool
    message: str
