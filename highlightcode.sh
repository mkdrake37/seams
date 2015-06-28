#!/bin/bash
pygmentize -S monokai -f html > css/syntax.scss
echo "---
---" | cat - css/syntax.scss > css/tmp && mv css/tmp css/syntax.scss