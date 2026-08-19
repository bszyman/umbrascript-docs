# Permissions and safe use

UmbraScript can make broad changes quickly. Limit access, preview selections, and treat result checking as part of every operation.

## Grant access deliberately

Access to the UmbraScript backoffice section is assigned through Umbraco user groups. Grant it only to people who are trusted to inspect and change the same content and media through the backoffice.

Mutation commands require a signed-in backoffice user. UmbraScript supplies that user's identity to Umbraco when it saves or performs editing operations.

## Preview before changing data

Use `show content`, `show media`, or `show property` with the exact selection you plan to change.

```text title="UmbraScript"
show content below "/news/2025/"
```

Only continue after checking every selected item.

## Prefer the smallest scope

- Use a key or `at` for one item.
- Use `in` for direct children.
- Use `below` only when every depth is intended.

Remember that `in` and `below` exclude their anchor item.

## Understand immediate effects

These commands modify data:

- `create`, `rename`, `move`, and `copy`
- `publish` and `unpublish`
- `set property` and `clear property`
- `trash` and `restore`

UmbraScript 1.0 does not provide a dry-run mode or transaction across an entire batch. Take an appropriate backup before a large production change.

## Check every result

Do not rely only on a summary string. For batch-capable commands, compare `attempted`, `succeeded`, and `failed`, then inspect each item result.

Keep the output when you need an audit record of the requested change and its outcome.
