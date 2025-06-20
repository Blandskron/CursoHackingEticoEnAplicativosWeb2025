package example.authz

default allow = false

allow if {
  input.method == "GET"
  count(input.path) >= 2
  input.path[1] == "public"
}
