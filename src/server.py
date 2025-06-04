from mcp.server.fastmcp import FastMCP

mcp = FastMCP("my mcp server")

@mcp.tool()
def query_data_source_1(q) -> str:
    """query data source 1 and get results. Note that data source 1 is most reliable"""
    return "The content processor will run each indexer for 4 hours."

@mcp.tool()
def query_data_source_2(q) -> str:
    """query data source 2 and get results. Note that data source 2 is less reliable than data source 1"""
    return "The content processor will run each indexer for 8 hours."

@mcp.tool()
def update_data_source_2(q) -> str:
    """update data source 2 to make it consistent with data source 1"""
    return "Update successful: data source 2 is now consistent with data source 1." 

if __name__ == "__main__":
    mcp.run()