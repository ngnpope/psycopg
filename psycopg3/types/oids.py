"""
Maps of builtin types and names

You can update this file by executing it, using the PG* env var to connect
to a Postgres server.
"""

# Copyright (C) 2020 The Psycopg Team

# typname, oid, array oid, regtype
_oids_table = [
    # autogenerated start
    # Generated from PostgreSQL 11
    ("abstime", 702, 1023, "abstime"),
    ("aclitem", 1033, 1034, "aclitem"),
    ("any", 2276, 0, '"any"'),
    ("anyarray", 2277, 0, "anyarray"),
    ("anyelement", 2283, 0, "anyelement"),
    ("anyenum", 3500, 0, "anyenum"),
    ("anynonarray", 2776, 0, "anynonarray"),
    ("anyrange", 3831, 0, "anyrange"),
    ("bit", 1560, 1561, "bit"),
    ("bool", 16, 1000, "boolean"),
    ("box", 603, 1020, "box"),
    ("bpchar", 1042, 1014, "character"),
    ("bytea", 17, 1001, "bytea"),
    ("char", 18, 1002, '"char"'),
    ("cid", 29, 1012, "cid"),
    ("cidr", 650, 651, "cidr"),
    ("circle", 718, 719, "circle"),
    ("cstring", 2275, 1263, "cstring"),
    ("date", 1082, 1182, "date"),
    ("daterange", 3912, 3913, "daterange"),
    ("event_trigger", 3838, 0, "event_trigger"),
    ("float4", 700, 1021, "real"),
    ("float8", 701, 1022, "double precision"),
    ("gtsvector", 3642, 3644, "gtsvector"),
    ("inet", 869, 1041, "inet"),
    ("int2", 21, 1005, "smallint"),
    ("int2vector", 22, 1006, "int2vector"),
    ("int4", 23, 1007, "integer"),
    ("int4range", 3904, 3905, "int4range"),
    ("int8", 20, 1016, "bigint"),
    ("int8range", 3926, 3927, "int8range"),
    ("internal", 2281, 0, "internal"),
    ("interval", 1186, 1187, "interval"),
    ("json", 114, 199, "json"),
    ("jsonb", 3802, 3807, "jsonb"),
    ("line", 628, 629, "line"),
    ("lseg", 601, 1018, "lseg"),
    ("macaddr", 829, 1040, "macaddr"),
    ("macaddr8", 774, 775, "macaddr8"),
    ("money", 790, 791, "money"),
    ("name", 19, 1003, "name"),
    ("numeric", 1700, 1231, "numeric"),
    ("numrange", 3906, 3907, "numrange"),
    ("oid", 26, 1028, "oid"),
    ("oidvector", 30, 1013, "oidvector"),
    ("opaque", 2282, 0, "opaque"),
    ("path", 602, 1019, "path"),
    ("point", 600, 1017, "point"),
    ("polygon", 604, 1027, "polygon"),
    ("record", 2249, 2287, "record"),
    ("refcursor", 1790, 2201, "refcursor"),
    ("reltime", 703, 1024, "reltime"),
    ("smgr", 210, 0, "smgr"),
    ("text", 25, 1009, "text"),
    ("tid", 27, 1010, "tid"),
    ("time", 1083, 1183, "time without time zone"),
    ("timestamp", 1114, 1115, "timestamp without time zone"),
    ("timestamptz", 1184, 1185, "timestamp with time zone"),
    ("timetz", 1266, 1270, "time with time zone"),
    ("tinterval", 704, 1025, "tinterval"),
    ("trigger", 2279, 0, "trigger"),
    ("tsquery", 3615, 3645, "tsquery"),
    ("tsrange", 3908, 3909, "tsrange"),
    ("tstzrange", 3910, 3911, "tstzrange"),
    ("tsvector", 3614, 3643, "tsvector"),
    ("txid_snapshot", 2970, 2949, "txid_snapshot"),
    ("unknown", 705, 0, "unknown"),
    ("uuid", 2950, 2951, "uuid"),
    ("varbit", 1562, 1563, "bit varying"),
    ("varchar", 1043, 1015, "character varying"),
    ("void", 2278, 0, "void"),
    ("xid", 28, 1011, "xid"),
    ("xml", 142, 143, "xml"),
    # autogenerated end
]

type_oid = {name: oid for name, oid, _, _ in _oids_table}


def self_update():
    import subprocess as sp

    # queries output should make black happy
    queries = [
        """
select format('    # Generated from PostgreSQL %s', setting::int / 10000)
    from pg_settings
    where name = 'server_version_num'
""",
        r"""
select format(
        '    ("%s", %s, %s, %s),',
        typname, oid, typarray,
        case when oid::regtype::text ~ '^"'
            then '''' || oid::regtype::text || ''''
            else '"' || oid::regtype::text || '"'
        end)
    from pg_type
    where oid < 10000
    and typname !~ all('{^(_|pg_|reg),_handler$}')
    order by typname
""",
    ]

    with open(__file__, "rb") as f:
        lines = f.read().splitlines()

    new = []
    for query in queries:
        out = sp.run(
            ["psql", "-AXqt", "-c", query], stdout=sp.PIPE, check=True
        )
        new.extend(out.stdout.splitlines())

    (istart,) = [
        i for i, l in enumerate(lines) if b"autogenerated " + b"start" in l
    ]
    (iend,) = [
        i for i, l in enumerate(lines) if b"autogenerated " + b"end" in l
    ]
    lines[istart + 1 : iend] = new

    with open(__file__, "wb") as f:
        f.write(b"\n".join(lines))
        f.write(b"\n")


if __name__ == "__main__":
    self_update()