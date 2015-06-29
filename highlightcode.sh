#!/bin/bash
pygmentize -S monokai -f html > css/tmp
cat css/head.scss css/tmp > css/syntax.scss
rm css/tmp