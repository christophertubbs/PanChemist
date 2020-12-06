# PanChemist
Pandas-Database intergration without SQLAlchemy

## WHY?!

`SQLAlchemy` is a great framework, but it does not *specialize* in simple, pandas focused database operations. 
It is very good for ORMs, but it overkill for basic interaction. If all you want is to apply some change to a 
database or get data from a database, now you have to understand how to use `SQLAlchemy`, which means you have 
to understand how every database builds connection strings, etc, etc. This is good if you're only doing it once, 
but the approach is a tad complicated when you a) aren't familiar with code to database integration and/or 
b) have to keep rewriting the same code to send semi-complicated data to the database (geospatial for instance).

## Goals

- [ ] Postgis integration
- [ ] Basic database data discovery (list tables, show table definitions, views, etc
- [ ] SQLite/Spatialite integration
- [ ] MySQL Integration
- [ ] MariaDB integration
- [ ] MongoDB Integration

## What's with the name?

I needed a name. I wanted `Pandas` in it since `Pandas` (and `GeoPandas` by extension) and I wanted to indicate 
that a database was involved and wasn't tied to `SQLAlchemy` or any sort of ORM tool. Pandb was taken, so I opted 
for a name like '`Pandas`, no `SQLAlchemy`'. It doesn't exactly roll off the tongue and smashing things together 
doesn't quite work, so what's almost the opposite or similar thing to an Alchemist? A Chemist. `PandasSQLChemist` 
or `PandasChemist` aren't quite right, thus, we get `PanChemist`, verbal emphasis on the `Pan` portion.
