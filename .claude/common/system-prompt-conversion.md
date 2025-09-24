# System Prompt Conversion Standard

## Standard Conversion Template

### **Phase 1: Document Structure Setup**
```yaml
---
name: [agent-identifier]
description: [When to use this agent - specific use cases and expertise areas]
model: [model-specification]
color: [ui-color]
---
```

### **Phase 2: System Prompt Framework**
```xml
<system_prompt>

# Methodology
<methodology>
You MUST first read and fully implement the pragmatic methodology located at:
@.claude/agents/common/pragmatic-principles.md

This file contains the complete development framework that you must follow for all tasks.

Before proceeding with any analysis or implementation:
1. Read the pragmatic methodology file using the Read tool
2. Internalize all phases and principles
3. Apply the framework systematically to the task at hand
</methodology>

# Agent Role
<role>
[Single paragraph defining the agent's primary identity, experience level, and recognition/authority]
</role>

<technical_expertise>
<core_technologies>
[3-5 primary technologies with specific expertise areas]
</core_technologies>

<[domain_specific_section]>
[Additional technical areas relevant to the role]
</[domain_specific_section]>

<additional_tools>
[Supporting tools and frameworks]
</additional_tools>
</technical_expertise>

<personality_traits>
[5-7 key behavioral characteristics using action-oriented language]
</personality_traits>

<response_guidelines>
<communication_style>
[Specific behavioral directives for how to communicate]
</communication_style>

<[domain]_standards>
[Standards specific to the domain/role]
</[domain]_standards>
</response_guidelines>

<instructions>
When responding to queries:
[Numbered list of 5-7 specific behavioral instructions]
</instructions>

# Tools
<tools>
You MUST read and fully implement the tool usage guidance located at:
@.claude/common/tool-usage-guide.md
</tools>

</system_prompt>
```

---

## Conversion Process

### **Step 1: Extract & Organize**
- [ ] Identify role/persona from original content
- [ ] Categorize technical skills into logical groupings
- [ ] Convert personality descriptions into actionable traits
- [ ] Transform communication style into behavioral directives

### **Step 2: Apply XML Structure**
- [ ] Use semantic tags that reflect the content hierarchy
- [ ] Nest related concepts appropriately
- [ ] Ensure all major sections have clear boundaries
- [ ] Use consistent naming conventions

### **Step 3: Optimize Language**
- [ ] Convert descriptive text to imperative instructions
- [ ] Use bullet points for easy parsing
- [ ] Include specific examples and context
- [ ] Add "when relevant" qualifiers for flexibility

### **Step 4: Integration**
- [ ] Add methodology reference with mandatory reading
- [ ] Include tool usage directive
- [ ] Create appropriate YAML frontmatter
- [ ] Ensure external dependencies are documented

### **Step 5: Validation**
- [ ] Verify all expertise areas are preserved
- [ ] Check that personality traits translate to behaviors
- [ ] Ensure instructions are specific and actionable
- [ ] Confirm external references are correct

---

## Key Principles for Future Conversions

### **XML Best Practices**
1. **Semantic Naming**: Tags should reflect content purpose, not presentation
2. **Logical Nesting**: Group related concepts under parent containers
3. **Consistent Structure**: Use same organization pattern across agents
4. **Clear Boundaries**: Each section should have distinct, non-overlapping content

### **Language Optimization**
1. **Imperative Voice**: "Provide", "Explain", "Consider" rather than "You should"
2. **Specific Behaviors**: "Include code examples" vs "Be helpful with code"
3. **Contextual Qualifiers**: "when relevant", "if applicable", "where appropriate"
4. **Action-Oriented**: Focus on what to DO rather than what to BE

### **Content Organization**
1. **Identity First**: Role and expertise establish context
2. **Behavior Second**: How to act and communicate
3. **Standards Third**: Quality and technical requirements
4. **Instructions Last**: Specific execution directives

### **Integration Considerations**
1. **External Dependencies**: Document all @.claude/ references
2. **Mandatory Sequences**: Use "MUST" for required pre-steps
3. **Systematic Approach**: Force methodology adoption before task execution
4. **Consistency**: Shared frameworks ensure uniform behavior across agents

This standard ensures consistent, high-quality system prompt conversions while maintaining the flexibility to specialize for different domains and use cases.
