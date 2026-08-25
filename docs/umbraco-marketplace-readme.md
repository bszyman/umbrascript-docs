# UmbraScript

UmbraScript is a talk-like scripting language for inspecting and automating content and media in Umbraco CMS.

Use readable statements in a dedicated backoffice section to inspect a tree, update properties, publish a branch, or organize media without building a one-off application.

![The UmbraScript editor in the Umbraco backoffice](https://www.umbrascript.org/media/umbrascript-editor.png)

## What you can do

- Inspect, create, publish, unpublish, rename, move, copy, trash, and restore content.
- Read, set, and clear content property values by alias.
- Inspect and organize media, including creating folders and moving items.
- Target one item by key or path, its direct children, or all of its descendants.
- Review structured JSON results with per-item outcomes for batch operations.

UmbraScript uses familiar Umbraco concepts such as content routes, content keys, Document Type aliases, property aliases, and the content and media trees. Keywords are case-insensitive, while names, paths, aliases, and values are written as quoted strings.

## See it in action

Inspect one content item without changing it:

```text
show content at "/destinations/pensacola-florida/"
```

Inspect every descendant below a branch:

```text
show content below "/news/"
```

Update a property on the direct children of an item:

```text
set property "region" of content in "/destinations/" to "Midwest"
```

Publish every descendant below a branch:

```text
publish content below "/news/"
```

Move a media item into another folder:

```text
move media at "/Images/legacy-logo.png" to at "/Images/Archive/"
```

## Install

UmbraScript is free to use with Umbraco CMS 17 and later.

Add the package to the directory containing your Umbraco project:

```console
dotnet add package UmbraScript
```

Build and restart the website. Then, as an administrator, open **Users**, select the appropriate user group, and enable the **UmbraScript** section under **Assign access**. Sign out and back in if the section does not appear immediately.

[Read the complete installation guide](https://www.umbrascript.org/get-started/install/)

## Start safely

UmbraScript can make broad changes quickly. Begin with a read-only command such as `show content`, `show media`, or `show property`, and use the same target or selection to inspect the affected items before running a command that changes data.

UmbraScript 1.0 does not provide a dry-run mode or a transaction across an entire batch. Check every per-item outcome and take an appropriate backup before making large production changes.

[Run the five-minute first-command tutorial](https://www.umbrascript.org/get-started/first-command/)

## Requirements and current scope

- Umbraco CMS 17 or later
- One statement per execution
- Content, property, and media commands
- JSON results

UmbraScript 1.0 does not currently define variables, comments, control flow, or multi-statement scripts. Property commands operate on content rather than media, and property changes save content without publishing it.

## Learn more

- [Documentation](https://www.umbrascript.org/)
- [Language guide](https://www.umbrascript.org/language/)
- [Command reference](https://www.umbrascript.org/reference/)
- [Permissions and safe use](https://www.umbrascript.org/administration/permissions-and-safety/)
- [Compatibility and limitations](https://www.umbrascript.org/administration/compatibility/)

UmbraScript is created by [Ben Szymanski](https://www.bszyman.com). If it saves you time, you can [support its development](https://buy.stripe.com/aFa9AVdqFbydbgz0Ve2Ry03).
