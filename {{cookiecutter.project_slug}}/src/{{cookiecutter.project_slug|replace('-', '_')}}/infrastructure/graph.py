{%- if cookiecutter.cache_backend == 'falkordb' -%}
{% raw %}
"""FalkorDB graph infrastructure.

Provides graph database operations using FalkorDB (Redis + Graph).
Use for relationship modeling, traversals, and graph algorithms.
"""

from __future__ import annotations

from typing import Any

from falkordb import FalkorDB

from .config import get_settings

# Graph client (initialized lazily)
_graph_client: FalkorDB | None = None
_graph_name = "app"


def get_graph_client() -> FalkorDB:
    """Get or create the FalkorDB client."""
    global _graph_client
    if _graph_client is None:
        settings = get_settings()
        if settings.redis_url is None:
            raise ValueError("REDIS_URL is not configured for FalkorDB")

        # Parse redis URL for host/port
        # Format: redis://host:port/db
        url = settings.redis_url
        if url.startswith("redis://"):
            url = url[8:]
        host_port = url.split("/")[0]
        host, port = host_port.split(":") if ":" in host_port else (host_port, "6379")

        _graph_client = FalkorDB(host=host, port=int(port))
    return _graph_client


def get_graph(name: str | None = None):
    """Get a graph instance by name."""
    client = get_graph_client()
    return client.select_graph(name or _graph_name)


async def init_graph() -> None:
    """Initialize the graph and create indexes."""
    graph = get_graph()

    # Create indexes for common node types
    # User nodes indexed by id for fast lookups
    try:
        graph.query("CREATE INDEX FOR (u:User) ON (u.id)")
    except Exception:
        pass  # Index may already exist


async def close_graph() -> None:
    """Close the FalkorDB connection."""
    global _graph_client
    if _graph_client is not None:
        _graph_client.close()
        _graph_client = None


class GraphRepository:
    """Base repository for graph operations.

    Provides common patterns for syncing entities to graph
    and querying relationships.
    """

    def __init__(self, graph_name: str | None = None):
        self.graph_name = graph_name

    @property
    def graph(self):
        return get_graph(self.graph_name)

    def create_node(self, label: str, properties: dict[str, Any]) -> None:
        """Create a node with given label and properties.

        Example:
            repo.create_node("User", {"id": "123", "name": "Alice"})
        """
        props = ", ".join(f"{k}: ${k}" for k in properties.keys())
        query = f"CREATE (n:{label} {{{props}}})"
        self.graph.query(query, properties)

    def update_node(self, label: str, node_id: str, properties: dict[str, Any]) -> None:
        """Update a node's properties.

        Example:
            repo.update_node("User", "123", {"name": "Bob"})
        """
        set_clause = ", ".join(f"n.{k} = ${k}" for k in properties.keys())
        query = f"MATCH (n:{label} {{id: $id}}) SET {set_clause}"
        self.graph.query(query, {"id": node_id, **properties})

    def delete_node(self, label: str, node_id: str) -> None:
        """Delete a node and all its relationships.

        Example:
            repo.delete_node("User", "123")
        """
        query = f"MATCH (n:{label} {{id: $id}}) DETACH DELETE n"
        self.graph.query(query, {"id": node_id})

    def create_edge(
        self,
        from_label: str,
        from_id: str,
        rel_type: str,
        to_label: str,
        to_id: str,
        properties: dict[str, Any] | None = None,
    ) -> None:
        """Create a relationship between two nodes.

        Example:
            repo.create_edge("User", "123", "FOLLOWS", "User", "456")
        """
        props = ""
        params = {"from_id": from_id, "to_id": to_id}
        if properties:
            props = " {" + ", ".join(f"{k}: ${k}" for k in properties.keys()) + "}"
            params.update(properties)

        query = f"""
            MATCH (a:{from_label} {{id: $from_id}})
            MATCH (b:{to_label} {{id: $to_id}})
            CREATE (a)-[r:{rel_type}{props}]->(b)
        """
        self.graph.query(query, params)

    def delete_edge(
        self,
        from_label: str,
        from_id: str,
        rel_type: str,
        to_label: str,
        to_id: str,
    ) -> None:
        """Delete a relationship between two nodes.

        Example:
            repo.delete_edge("User", "123", "FOLLOWS", "User", "456")
        """
        query = f"""
            MATCH (a:{from_label} {{id: $from_id}})-[r:{rel_type}]->(b:{to_label} {{id: $to_id}})
            DELETE r
        """
        self.graph.query(query, {"from_id": from_id, "to_id": to_id})

    def query(self, cypher: str, params: dict[str, Any] | None = None) -> list[dict]:
        """Execute a raw Cypher query and return results.

        Example:
            results = repo.query(
                "MATCH (u:User)-[:FOLLOWS]->(f:User) WHERE u.id = $id RETURN f.name",
                {"id": "123"}
            )
        """
        result = self.graph.query(cypher, params or {})
        return [dict(zip(result.header, row)) for row in result.result_set]
{% endraw %}
{%- else -%}
"""Graph infrastructure - Not enabled.

This project was generated without FalkorDB graph support.
To enable graph capabilities, regenerate with cache_backend='falkordb'.
"""
{%- endif %}
