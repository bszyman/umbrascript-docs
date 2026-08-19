# Statements and keywords

UmbraScript 1.0 accepts one statement per execution. A statement must use the expected words in the expected order.

```text title="UmbraScript"
rename content at "/news/old-title/" to "New title"
```

## One statement at a time

The parser expects the statement to end after the command is complete. A second statement or unexplained text produces an error.

```text
show content at "/news/" publish content at "/news/"
```

Run these as two separate submissions instead.

## Keywords are case-insensitive

The following statements have the same meaning:

```text title="UmbraScript"
show media in "/Images/"
```

```text title="UmbraScript"
SHOW MEDIA IN "/Images/"
```

Lowercase keywords are used throughout this documentation for consistency.

## Whitespace is flexible

Spaces, tabs, and line breaks separate tokens. They do not change the meaning of a valid statement.

```text title="UmbraScript"
create content
named "Release notes"
of type "article"
at "/news/"
```

## Reserved words

UmbraScript 1.0 recognizes these words:

| Actions | Resources and grammar |
| --- | --- |
| `show`, `publish`, `unpublish`, `trash`, `restore`, `rename`, `clear`, `move`, `copy`, `create`, `set` | `content`, `media`, `folder`, `property`, `properties`, `name`, `named`, `at`, `below`, `in`, `with`, `type`, `of`, `to`, `root` |

Names, aliases, paths, keys, and values are not keywords. Write them as [quoted strings](strings.md).

## Comments and variables

UmbraScript 1.0 does not define comments, variables, or multi-statement scripts. Characters or words outside the supported grammar produce a diagnostic.
