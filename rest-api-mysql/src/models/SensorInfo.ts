import { Model, InferAttributes, InferCreationAttributes, DataTypes } from 'sequelize';
import {sequelizeConnection} from '../db/config';

// order of InferAttributes & InferCreationAttributes is important.
class SensorData extends Model {
  // 'CreationOptional' is a special type that marks the field as optional
  // when creating an instance of the model (such as using Model.create()).
  declare entry_id: number;
  declare temp: string | null;
  declare hum: string | null;
  // other attributes...
}

SensorData.init(
    {
        entry_id: {
            type: DataTypes.INTEGER,
            autoIncrement: true,
            primaryKey: true,
        },
        temp: {
            type: new DataTypes.STRING(128),
            allowNull: true,
        },
        hum: {
            type: new DataTypes.STRING(128),
            allowNull: true,
        },
    }, 
    {
        tableName: 'sensor_data_12',
        sequelize: sequelizeConnection,
    }
)

export default SensorData;
