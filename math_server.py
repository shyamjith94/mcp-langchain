from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="math-server",)


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers
    params:
    a: int
    b: int

    return:
        c:int  a + b
    """

    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Add two numbers
    params:
    a: int
    b: int

    return:
        c:int  a * b
    """

    return a * b

if __name__ == "__main__":
    # stdio use standard input and output stdin stdout to receive and respond to tool function calls
    mcp.run(transport="stdio")