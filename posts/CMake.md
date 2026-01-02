---
layout: post
render_with_liquid: false
date: 2025-12-26
title: "CMake"
unlisted: true
---

### Convert a binary file directly to object file

    objcopy --input binary \
        --output elf32-i386 \
        --binary-architecture i386 foo foo.o

(see <https://unix.stackexchange.com/a/176271>)

### Custom Python step in CMake build

<https://gist.github.com/mcejp/06d225ae1620bdf0148eee6ec9db8e3b>

### Deep clean of build directories

Clean all `cmake-build*` directories:

    find . -type d -name "cmake-build*" \
        -exec sh -c 'cd "{}" && make clean' \;

Delete all `cmake-build*` directories:

    find . -type d -name "cmake-build*" \
        -ok rm -r -- {} \;

### Disassemble executable after build

``` cmake
set(LISTING_PATH $<TARGET_FILE:${CMAKE_PROJECT_NAME}>)
cmake_path(REPLACE_EXTENSION LISTING_PATH ".s")
add_custom_command(
    TARGET ${CMAKE_PROJECT_NAME} POST_BUILD
    COMMAND
        ${CMAKE_OBJDUMP} $<TARGET_FILE:${CMAKE_PROJECT_NAME}> --all-headers --disassemble > ${LISTING_PATH}
    COMMENT
        "Disassembling executable $<TARGET_FILE:${CMAKE_PROJECT_NAME}>")
```

### Embed a binary file in a C++ header as span\<uint8_t\>

1.  Grab
    [FileEmbed.cmake](https://gist.github.com/mcejp/52b1a5529dee3cb5bac2a27d1aa2dc06)
2.  Use it like this:

``` cmake
include(FileEmbed.cmake)

# Generated files should be considered byproducts of the build (same as e.g. object files) and as such, should go somewhere under BINARY_DIR
FileEmbed_Add(schema.xsd
              "${CMAKE_CURRENT_BINARY_DIR}/schema.hpp"
              the_schema)

# Make sure the path is among the include directories
target_include_directories(my_target PRIVATE
                           "${CMAKE_CURRENT_BINARY_DIR}")
```

### Embed a binary file in a C header using xxd at build time

(untested! but based on well-known patterns)

``` cmake
function(xxd_generate_header SOURCE OUTPUT)
    get_filename_component(SOURCE ${SOURCE} ABSOLUTE)

    # Watch out: This breaks if multiple targets reference $OUTPUT:
    # https://cmake.org/cmake/help/latest/command/add_custom_command.html#example-generating-files-for-multiple-targets
    add_custom_command(
        OUTPUT
            "${OUTPUT}"
        COMMAND
            xxd --include "${SOURCE}" > "${OUTPUT}"
        DEPENDS
            "${SOURCE}"
        )
endfunction()
```

### Optional dependencies

See here: <https://sarcasm.github.io/notes/dev/cmake.html#id7>
