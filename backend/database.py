import asyncio
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
database = client['TodoList']
collection = database['todo']

async def fetch_one_todo(title):
    loop = asyncio.get_event_loop()
    document = await loop.run_in_executor(None, collection.find_one, {"title": title})
    return document

async def fetch_all_todos():
    loop = asyncio.get_event_loop()
    todos = await loop.run_in_executor(None, list, collection.find({}))
    return todos

async def create_todo(todo):
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, collection.insert_one, todo)
    return todo

async def update_todo(title, desc):
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, collection.update_one, {"title": title}, {"$set": {"description": desc}})
    document = await fetch_one_todo(title)
    return document

async def remove_todo(title):
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, collection.delete_one, {"title": title})
    return result.deleted_count > 0
