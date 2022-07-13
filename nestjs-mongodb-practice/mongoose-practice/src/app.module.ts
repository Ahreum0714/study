import { Module } from '@nestjs/common';
import { MongooseModule } from '@nestjs/mongoose';

import { AppController } from './app.controller';
import { AppService } from './app.service';
import { ProductsModule } from './products/products.module';

@Module({
  imports: [
    ProductsModule,
    MongooseModule.forRoot(
      // 'mongodb+srv://maximilian:B3dqPzooRLzFiVYm@cluster0-ntrwp.mongodb.net/nestjs-demo?retryWrites=true&w=majority',
      'mongodb://localhost:27017/test2',
      { useNewUrlParser: true },
    ),
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
