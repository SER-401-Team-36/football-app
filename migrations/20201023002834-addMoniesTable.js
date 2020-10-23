'use strict';

var dbm;
var type;
var seed;

/**
 * We receive the dbmigrate dependency from dbmigrate initially.
 * This enables us to not have to rely on NODE_PATH.
 */
exports.setup = function (options, seedLink) {
  dbm = options.dbmigrate;
  type = dbm.dataType;
  seed = seedLink;
};

exports.up = function (db) {
  return db.createTable('monies', {
    id: { type: 'int', primaryKey: true, autoIncrement: true },
    units: { type: 'int', notNull: true },
    currency: { type: 'string', notNull: true },
  });
};

exports.down = function (db) {
  return db.dropTable('monies');
};

exports._meta = {
  version: 1,
};
