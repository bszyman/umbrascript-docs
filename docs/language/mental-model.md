# Mental model

UmbraScript is a small, task-focused language that maps readable statements onto Umbraco CMS operations.

It is inspired by the approachable command style of [HyperTalk](https://en.wikipedia.org/wiki/HyperTalk), [AppleScript](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptX/AppleScriptX.html), and [Hyperscript](https://hyperscript.org/), but its vocabulary and data model are designed around Umbraco.

## Action, resource, and target

Most statements have three parts:

```text title="UmbraScript"
show content below "/destinations/"
```

- `show` describes the action.
- `content` describes the resource.
- `below "/destinations/"` describes the target selection.

Commands that change a value or location add another clause:

```text title="UmbraScript"
rename content at "/news/old-title/" to "New title"
```

UmbraScript is readable, but it is not free-form natural language. The parser accepts a defined vocabulary and word order so that each statement has one predictable meaning.

## Trees are the organizing model

Content and media are addressed as trees. A statement can target:

- One item by key or path
- The direct children of an item
- Every descendant of an item
- A root or parent destination

The same selection concepts are reused by read commands and batch-capable mutation commands. This lets you preview with `show` before applying a change.

## Umbraco remains the source of truth

UmbraScript does not create a second content model. Document Type aliases, property aliases, routes, keys, culture behavior, editing operations, and operation outcomes come from Umbraco CMS.

The language translates a statement into an Umbraco operation and returns structured JSON describing what was read or attempted.

## Small language, explicit effects

UmbraScript 1.0 intentionally focuses on one statement at a time. There are no variables, loops, or hidden multi-step workflows. Batch behavior comes from explicit tree selections such as `in` and `below`.

Continue with [Statements and keywords](statements.md) for the lexical rules or [References and selections](references-and-selections.md) for the tree grammar.
