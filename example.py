"""Run an example script to quickly test."""
import asyncio

from aiohttp import ClientSession

from pyden import Client
from pyden.errors import PydenError

GOOGLE_API_KEY = 'AIzaSyA_V6RUweRcy2wz_D1fwbO1rXaSrnQ3BmA'
LATITUDE = 39.7974509
LONGITUDE = -104.8887227


async def trash(client: Client) -> None:
    """Output allergen-related information."""
    await client.trash.init_from_coords(LATITUDE, LONGITUDE, GOOGLE_API_KEY)

    print('UPCOMING TRASH SCHEDULE')
    schedule = await client.trash.upcoming_schedule()
    for date, types in schedule.items():
        print(
            '{0}: {1}'.format(date, [t.value for t, v in types.items() if v]))

    print()
    print('NEXT DATE FOR TRASH')
    print(await client.trash.next_pickup(client.trash.PickupTypes.trash))

    print()
    print('NEXT DATE FOR EXTRA TRASH')
    print(await client.trash.next_pickup(client.trash.PickupTypes.extra_trash))

    print()
    print('NEXT DATE FOR RECYCLING')
    print(await client.trash.next_pickup(client.trash.PickupTypes.recycling))

    print()
    print('NEXT DATE FOR COMPOST')
    print(await client.trash.next_pickup(client.trash.PickupTypes.compost))


async def main() -> None:
    """Create the aiohttp session and run the example."""
    async with ClientSession() as websession:
        await run(websession)


async def run(websession):
    """Run."""
    try:
        # Create a client:
        client = Client(websession)

        # Work with trash data:
        await trash(client)
    except PydenError as err:
        print(err)


asyncio.get_event_loop().run_until_complete(main())
