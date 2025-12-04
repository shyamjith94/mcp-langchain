from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="weather-server")

async def get_weather(location: str) -> str:
    """getting whether based location
    params:
    location: str

    return:
        weather: str
    """

    return "rainy"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")