# 1: understand the context information to execute tasks

## 1-1: paths

- source: .agent/source/japanese/
- dist: .agent/dist/

# 2: execute tasks

## 2-1: translate task

translate all files and directories in the path "source" to the path "dist", recursively.

- translate from japanese to english
- the translate results should be written in english.
- translate if the update time of the path "dist" are newer than the path "source".

## 2-2: cleanup task

Delete the files and directories that exist in the path "dist" but not in the path "source".
