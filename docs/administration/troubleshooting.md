# Troubleshooting

## The UmbraScript section is missing

1. Confirm that the package is referenced by the Umbraco project.
2. Rebuild and restart the website.
3. Confirm that the user's group has access to the UmbraScript section under **Users** and **User Groups**.
4. Sign out and back in after changing group access.

## A path does not resolve

For content:

- Begin the route with `/`.
- Use `at` for a single-item path reference.
- Confirm the route in the website's default culture.

For media:

- Follow media item names from the media root.
- Ensure each path segment has a unique matching sibling.
- Use the media key if a name is ambiguous.

See [References and selections](../language/references-and-selections.md).

## A key is rejected

A bare quoted reference must be a GUID:

```text title="UmbraScript"
show content "b01b9237-ca8d-499a-aa97-de894cab5e3b"
```

A path without `at` is interpreted as a key and produces `US3001`.

## A command selected too many items

Rename, move, copy, trash, and restore commands operate on one item. Use a key or `at "<path>"`, not `in` or `below`.

## A property update failed

Check the per-item result:

- `propertyExists` indicates whether the content type contains the alias.
- `oldValue` and `newValue` show the attempted change.
- `outcome` contains the Umbraco operation result.

Confirm that the property editor accepts a string in the supplied format. Variant properties require additional care because UmbraScript 1.0 does not select a culture or segment.

## A batch only partially succeeded

Compare `attempted`, `succeeded`, and `failed`, then inspect every per-item outcome. Do not assume that successful earlier changes were rolled back. Resolve the individual failures and retry only the items that still require the operation.
