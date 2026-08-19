# Language guide

UmbraScript statements read like short instructions. Each statement combines an action, a resource, and the information needed to identify or change that resource.

```text title="UmbraScript"
publish content below "/news/"
```

In this example:

- `publish` is the action.
- `content` is the resource.
- `below "/news/"` selects every descendant of the News item.

## Core concepts

- [Mental model](mental-model.md) explains how actions, resources, and tree targets fit together.
- [Statements and keywords](statements.md) explains word order, whitespace, and case sensitivity.
- [Strings](strings.md) explains quoted values and escape sequences.
- [References and selections](references-and-selections.md) explains keys, paths, `at`, `in`, and `below`.
- [Destinations](destinations.md) explains `root` and parent destinations for create, move, and copy commands.
- [Results and errors](results-and-errors.md) explains JSON results and diagnostic codes.

Use the [command reference](../reference/index.md) for the exact grammar and behavior of each statement.
