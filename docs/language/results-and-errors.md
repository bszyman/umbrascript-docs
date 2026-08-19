# Results and errors

UmbraScript returns structured JSON. Read commands return the selected data. Commands that change data report the attempted operation and its outcome.

## Read results

`show content` and `show media` return arrays. An `at` or key reference normally returns an array with one item; `in` and `below` can return several.

```json
{
  "content": [
    {
      "key": "b01b9237-ca8d-499a-aa97-de894cab5e3b",
      "id": 1138,
      "name": "Pensacola, Florida",
      "contentTypeAlias": "destination"
    }
  ]
}
```

## Mutation results

Batch-capable commands commonly include:

| Field | Meaning |
| --- | --- |
| `summary` or `requestedStatus` | The requested operation |
| `attempted` | Number of selected items processed |
| `succeeded` | Number of successful item operations |
| `failed` | Number of unsuccessful item operations |
| `content` or `results` | Per-item details |

Single-item commands include an item key and name plus fields such as `success`, `result`, `outcome`, or `message`.

!!! warning
    Do not treat a returned batch as transactional. Check `failed` and every per-item outcome. UmbraScript does not promise that earlier successful changes will be rolled back when another item fails.

## Language diagnostics

Language errors include a code and the line and column at which parsing failed.

| Code | Meaning |
| --- | --- |
| `US1001` | Unexpected character |
| `US1002` | Unterminated string |
| `US1003` | Invalid escape sequence |
| `US1004` | Unknown word |
| `US2001` | Expected a different token |
| `US2002` | Unexpected token |
| `US2003` | Expected a recognized statement |
| `US3001` | Invalid GUID key |
| `US3002` | The resource does not support the action |
| `US3003` | Unsupported reference |
| `US3004` | Expected `content` or `media` |

Runtime errors describe failures such as an item not being found, an ambiguous media path, a missing Document Type, or a command resolving more items than it supports. See [Troubleshooting](../administration/troubleshooting.md).
