# Organize media

Create a destination folder, inspect the source item, then move or copy it.

## Create a folder

Create an Archive folder below Images:

```text title="UmbraScript"
create media folder named "Archive" at "/Images/"
```

## Inspect the source

Check that the path identifies one item:

```text title="UmbraScript"
show media at "/Images/legacy-logo.png"
```

If sibling items share a name and the path is ambiguous, use the returned media key in later commands.

## Move or copy the item

Move the original:

```text title="UmbraScript"
move media at "/Images/legacy-logo.png" to at "/Images/Archive/"
```

Or create a copy with a new name:

```text title="UmbraScript"
copy media at "/Images/legacy-logo.png" to at "/Images/Archive/" with name "Legacy logo archive"
```

Copying media duplicates its stored file and property values. Check the result before removing the source.

## Verify the destination

```text title="UmbraScript"
show media in "/Images/Archive/"
```

Review the returned key, name, media type, dimensions, and file type.
