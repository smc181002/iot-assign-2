import { Router } from 'express';

import { getFeed, pushFeed } from '../controllers/feed.controller';

const router = Router();

router.get("/", getFeed);
router.get("/push/", pushFeed);

export default router;
