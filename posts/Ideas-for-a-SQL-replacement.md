---
layout: post
render_with_liquid: false
date: 2024-01-05
title: "Ideas for a SQL replacement"
unlisted: true
---

- <https://news.ycombinator.com/item?id=24337244>

<!-- -->


    select(sort(
        filter(table(users), \ u: u.name == $1),
        \ u: u.id))

    or:

      table(users) filter(name == $1) sort(id, ASC)
      table(users) filter(id == $1) update(salary = 10000)

    select(join(table(user), table(department), \ u, d: d.id == u.department_id))

    insert(table(user), {
      id: 1,
      name: "Foo"
      })

Low-level intermediate representation?

    SELECT_FROM users: id, name
    FILTER
      LOAD_COLUMN users.name
      LOAD_PARAMETER $1
      EQ
      RET
    SORT users.id ASC
