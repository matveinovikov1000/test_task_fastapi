from typing import Annotated
from fastapi import Depends, APIRouter, status, Response, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from schemas.schemas import AddURL, ShortIdURL
from db.database import get_session
from models.models import URL
from services.service import generate_short_id

router = APIRouter()

SessionDep = Annotated[AsyncSession, Depends(get_session)]


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_short_url(url_sch: AddURL, session: SessionDep):
    """Принимает URL и сокращает его"""
    url_org = str(url_sch.url)
    get_url = await session.execute(select(URL).where(URL.url == url_org))
    current_url = get_url.scalars().first()

    if current_url:
        return {"short_id": current_url.short_id}

    while True:
        short_id = generate_short_id()
        get_url_two = await session.execute(select(URL).where(URL.short_url == short_id))
        if not get_url_two.scalars().first():
            break

    new_url = URL(url=url_org, short_url=short_id)
    session.add(new_url)
    await session.commit()
    await session.refresh(new_url)
    return {"short_id": new_url.short_url}


@router.get("/{short_id}", status_code=status.HTTP_307_TEMPORARY_REDIRECT)
async def return_url(short_id: str, session: SessionDep):
    """Принимает идентификатор сокращенного URL и возвращает исходный URL"""
    get_url = await session.execute(select(URL).where(URL.short_url == short_id))
    url_obj = get_url.scalars().first()
    if not url_obj:
        raise HTTPException(status_code=404, detail="URL not found")
    return Response(
        status_code=status.HTTP_307_TEMPORARY_REDIRECT,
        headers={"Location": url_obj.url},
    )
