redis-cli keys '*' | while read key; do echo "$key -> $(redis-cli get $key)"; done
