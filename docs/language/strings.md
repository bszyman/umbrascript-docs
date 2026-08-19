# Strings

Write keys, paths, names, aliases, and property values inside double quotation marks.

```text title="UmbraScript"
set property "pageTitle" of content at "/news/" to "Today's news"
```

## Escape sequences

Use a backslash when a string must contain a quotation mark, backslash, or control character.

| Sequence | Value |
| --- | --- |
| `\"` | Double quotation mark |
| `\\` | Backslash |
| `\n` | Line feed |
| `\r` | Carriage return |
| `\t` | Tab |

For example:

```text title="UmbraScript"
rename content at "/news/todays-news/" to "Today's \"Top Story\""
```

An unsupported escape sequence produces diagnostic `US1003`. A missing closing quotation mark produces `US1002`.

## Property values

Property commands accept the new value as a string, even when the property represents a number or another data type.

```text title="UmbraScript"
set property "latitude" of content at "/destinations/chicago/" to "41.8781"
```

The Umbraco property editor determines how the value is stored. Test property updates on representative content before applying them to a selection.
