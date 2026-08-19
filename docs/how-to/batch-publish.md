# Publish content in batches

Publish direct children or every descendant of a content item, then check the per-item outcome.

## Preview the selection

Run `show content` first:

```text title="UmbraScript"
show content below "/news/2025/"
```

Confirm that the list contains every item you intend to publish and no others. `below` includes all depths but excludes the `/news/2025/` anchor.

## Publish the selection

Use the same selection with `publish content`:

```text title="UmbraScript"
publish content below "/news/2025/"
```

Use `in` instead when you want only direct children:

```text title="UmbraScript"
publish content in "/news/2025/"
```

## Check the result

Verify that:

- `attempted` matches the previewed item count.
- `failed` is `0`.
- Every item in `content` has `success` set to `true`.

If an item fails, read its `outcome` before retrying. A successful item is not automatically rolled back because another item failed.

To reverse the operation, preview the same selection again and use [unpublish content](../reference/content/unpublish.md).
