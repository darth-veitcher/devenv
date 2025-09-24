## MCP Tool Usage Guide (including Hierarchy and Fallbacks)

<tool_hierarchy_best_practices>
<tool_selection_rules>
<web_research>
<primary>web_search</primary>
<fallback_1>mcp_searxng</fallback_1>
<fallback_2>mcp_crawl4ai</fallback_2>
<usage_note>Use WebSearch first, then SearXNG if WebSearch fails, then Crawl4AI for deep dives on specific pages</usage_note>
</web_research>

  <documentation>
    <primary>mcp_context7</primary>
    <required_for>FastAPI, Railway, Fly, Docker, and all official library documentation</required_for>
    <fallback_chain>web_search → mcp_searxng → mcp_crawl4ai</fallback_chain>
    <usage_note>ALWAYS use Context7 for official docs first. Use fallback chain only for tutorials/examples</usage_note>
  </documentation>

<code_analysis>
<primary>mcp_serena_find_symbol</primary>
<secondary>mcp_serena_search_for_pattern</secondary>
<session_requirement>mcp_serena_initial_instructions</session_requirement>
<usage_note>Serena tools are superior to Read for code analysis. MUST run initial_instructions at session start</usage_note>
</code_analysis>

<complex_tasks>
<planning>mcp_sequential_thinking</planning>
<execution>task_tool</execution>
<usage_note>Use sequential thinking for planning and analysis, Task tool for parallel agent work</usage_note>
</complex_tasks>

<container_management>
<tool>docker_mcp_server</tool>
<operations>
<create>create-container</create>
<deploy>deploy-compose</deploy>
<list>list-containers</list>
<logs>get-logs</logs>
</operations>
<usage_note>Test locally with Docker before deploying to production environments</usage_note>
</container_management>
</tool_selection_rules>

<required_usage_patterns>
<session_start>
<step_1>mcp_serena_initial_instructions()</step_1>
<step_2>mcp_serena_list_memories()</step_2>
<step_3>mcp_sequential_thinking("plan session")</step_3>
<mandatory>true</mandatory>
</session_start>

<feature_implementation>
<step_1>Sequential thinking (plan)</step_1>
<step_2>Context7 (check docs)</step_2>
<step_3>Serena (understand code)</step_3>
<step_4>Task tool (parallel implementation)</step_4>
<step_5>Docker (test locally before deploy)</step_5>
<workflow_type>sequential</workflow_type>
</feature_implementation>

<debug_session>
<step_1>Sequential thinking (analyze problem)</step_1>
<step_2>Serena search (find relevant code)</step_2>
<step_3>Docker get-logs (container errors)</step_3>
<step_4>WebSearch → SearXNG (research error patterns)</step_4>
<workflow_type>diagnostic</workflow_type>
</debug_session>
</required_usage_patterns>

<critical_mistakes_to_avoid>
<mistake>Using Fetch without Crawl4AI fallback</mistake>
<mistake>Skipping Context7 for library documentation</mistake>
<mistake>Not using Sequential thinking for complex tasks</mistake>
<mistake>Working sequentially instead of using Task tool for parallel work</mistake>
<mistake>Not checking Serena memories at session start</mistake>
<mistake>Not testing with Docker before production deployment</mistake>
</critical_mistakes_to_avoid>

<tool_performance_notes>
<web_fetch>
<reliability>low</reliability>
<fallback_required>mcp_crawl4ai</fallback_required>
<note>WebFetch often fails - always use Crawl4AI as backup</note>
</web_fetch>

  <context7>
    <performance>fastest</performance>
    <best_for>official documentation</best_for>
    <note>Fastest option for official library docs</note>
  </context7>

<task_tool>
<concurrency>up to 10 parallel agents</concurrency>
<best_for>complex multi-part implementations</best_for>
<note>Can run 10 agents in parallel for complex tasks</note>
</task_tool>

  <serena>
    <persistence>across sessions</persistence>
    <memory_type>project context and patterns</memory_type>
    <note>Memories persist across sessions - always check at start</note>
  </serena>
</tool_performance_notes>

<enforcement_rules>
<rule>Before any coding task, MUST check Context7 for relevant documentation</rule>
<rule>Before any debug session, MUST run Serena initial instructions and check memories</rule>
<rule>For any complex task (>3 steps), MUST use Sequential thinking for planning</rule>
<rule>For any web content retrieval failure, MUST try fallback chain before giving up</rule>
<rule>For any container deployment, MUST test locally with Docker first</rule>
</enforcement_rules>
</tool_hierarchy_best_practices>
