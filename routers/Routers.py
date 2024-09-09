from typing import Optional

from fastapi import APIRouter

from parser import Parser


router = APIRouter(prefix="/api/v1")


@router.get("/groups")
async def get_groups(date: Optional[str] = None):
    try:
        return Parser.get_groups(date=date)
    except Exception as ex:
        print(ex)
        return {
            "data": "error",
        }


@router.get("/archives")
async def get_archives(year: Optional[int] = None):
    try:
        return Parser.get_archives(year=year)
    except Exception as ex:
        print(ex)
        return {
            "data": "error",
        }


@router.get("/shedule")
async def get_shedule(group: str, date: Optional[str] = None):
    try:
        return Parser.get_page(group=group, date=date)
    except Exception as ex:
        print(ex)
        return {
            "data": "error",
        }
