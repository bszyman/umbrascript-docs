# Inspect a tree

Use `show content` or `show media` to find a key, check a path, or preview a selection before another command.

## Inspect one item

Reference the item by path:

```text title="UmbraScript"
show content at "/destinations/chicago/"
```

Copy the returned `key` when later commands should keep targeting the same item even if its route changes.

## List direct children

Use `in` to inspect one level below the anchor:

```text title="UmbraScript"
show content in "/destinations/"
```

For media, paths follow media item names:

```text title="UmbraScript"
show media in "/Images/Destinations/"
```

## List every descendant

Use `below` to include descendants at every depth:

```text title="UmbraScript"
show content below "/news/2025/"
```

Large trees can return large results. Start with `in` when you do not yet know the branch structure.

## Use the selection in another command

After verifying every returned item, reuse the portion after `content` or `media`:

```text title="UmbraScript"
publish content below "/news/2025/"
```

The [selection reference](../language/references-and-selections.md) describes all supported key and path forms.
