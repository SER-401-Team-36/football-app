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
  return db.createTable('loan_requests', {
    id: { type: 'int', primaryKey: true, autoIncrement: true },
    requestee_name: {
      type: 'string',
      required: true,
    },
    money_id: {
      type: 'int',
      notNull: true,
      foreignKey: {
        name: 'loan_requests_money_id_fk',
        table: 'monies',
        rules: {
          onDelete: 'CASCADE',
        },
        mapping: 'id',
      },
    },
    created_at: { type: 'datetime', required: true },
    updated_at: { type: 'datetime', required: true },
  });
};

exports.down = function (db) {
  return db.dropTable('loan_requests');
};

exports._meta = {
  version: 1,
};
