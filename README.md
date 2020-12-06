# PanChemist
Pandas-Database intergration without SQLAlchemy

## WHY?!

SQLAlchemy is a great framework, but it does not *specialize* in basic day-to-day database operations. It is very good for ORMs, but it overkill for basic interaction. If all you want is to apply some change to a database or get data from a database, now you have to understand how to use SQLAlchemy, which means you have to understand how every database builds connection strings, etc, etc. This is good if you're only doing it once, but the approach is a tad complicated when you a) aren't familiar with code to database integration and/or b) have to keep rewriting the same code to send semi-complicated data to the database (geospatial for instance).

## Goals

- [ ] Postgis integration
- [ ] Basic database data discovery
- [ ] SQLite/Spatialite integration
- [ ] MySQL Integration
- [ ] MariaDB integration
- [ ] MongoDB Integration
