import {Request, Response} from 'express';
import SensorData from '../models/SensorInfo';

export const getFeed = async (_: Request, res: Response) => {
    let data = await SensorData.findAll();
    res.json(data);
}

export const pushFeed = async (req: Request, res: Response) => {
    let data = req.query;
    let temp = data['field1'];
    let hum = data['field2'];

    const sensor = await SensorData.create({
        temp: parseInt(temp as string),
        hum: parseInt(hum as string),
    })

    res.json(sensor);
}
