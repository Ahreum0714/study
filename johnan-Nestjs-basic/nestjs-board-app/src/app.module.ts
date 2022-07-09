import { Module } from '@nestjs/common';
import { MongooseModule } from '@nestjs/mongoose';
// import { TypeOrmModule } from '@nestjs/typeorm';
import { BoardRepository } from './boards/board.repository';
import { BoardsModule } from './boards/boards.module';
import { typeORMConfig } from './configs/typeorm.config';

@Module({
  imports: [
    // TypeOrmModule.forRoot(typeORMConfig),
    MongooseModule.forRoot('mongodb://localhost/nest'),
    BoardsModule
  ],
})
export class AppModule {}
