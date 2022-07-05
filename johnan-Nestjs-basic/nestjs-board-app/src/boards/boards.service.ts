import { Injectable } from '@nestjs/common';
import { Board } from './boards.model';

@Injectable()
export class BoardsService {
  private boards: Board[] = []; // 다른 컴포넌트에서 boards 수정 못하도록 private 선언

  getAllBoards(): Board[] {
    return this.boards;
  }
}
