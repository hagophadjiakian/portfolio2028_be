from fastapi import APIRouter, HTTPException, status
from app.schemas.contact import ContactForm, ContactResponse
import logging

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/contact", response_model=ContactResponse)
async def submit_contact_form(form: ContactForm):
    """Handle contact form submissions."""
    try:
        logger.info(f"Contact form received from: {form.email}")

        # In production: save to database, send email, etc.

        return ContactResponse(
            success=True,
            message=f"Thank you, {form.name}! Your message has been received."
        )
    except Exception as e:
        logger.error(f"Error processing contact form: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while processing your message."
        )
