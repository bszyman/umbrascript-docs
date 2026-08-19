# Destinations

Create, move, and copy commands place an item under a destination parent or at the root of a tree.

## Move and copy destinations

Use one of these forms after `to`:

| Form | Destination |
| --- | --- |
| `to root` | The content or media root |
| `to "<key>"` | The item identified by a key |
| `to at "<path>"` | The item identified by a path |

```text title="UmbraScript"
move content at "/news/old-story/" to at "/archive/"
```

The repeated prepositions are intentional: `to` introduces the destination, and `at` introduces a path reference.

```text title="UmbraScript"
copy media at "/Images/logo.png" to root with name "Logo copy"
```

Content destinations are content nodes. Media destinations should normally be media folders.

## Create destinations

Create commands include `at` as part of their grammar. The forms are:

| Form | Destination |
| --- | --- |
| `at root` | The tree root |
| `at "<key>"` | The item identified by a key |
| `at "<path>"` | The item identified by a path |

```text title="UmbraScript"
create content named "Release notes" of type "article" at "/news/"
```

```text title="UmbraScript"
create media folder named "Archive" at root
```

Create commands do not use `at at` before a path.
