# Migrating from symjoy 1.x to 2.x

symjoy 2.x introduces a structured API while preserving backward compatibility.

## What Changed

-   Raw dictionaries are replaced by category APIs
-   Global search is now available
-   Metadata (category, unicode) is exposed

## What Still Works

-   `emojis["smile"]` (deprecated)
-   All original symbol names

## What Will Be Removed in 3.0.0

-   Direct dictionary access
