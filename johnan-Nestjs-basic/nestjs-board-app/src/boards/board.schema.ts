import { Prop, Schema, SchemaFactory } from "@nestjs/mongoose";
import { BoardStatus } from "./board-status.enum";
import { Document } from "mongoose";

export type BoardDocument = Board & Document;

@Schema()
export class Board {
    @Prop()
    title: string;

    @Prop()
    description: string;
    
    @Prop()
    status: BoardStatus;
}

export const BoardSchema = SchemaFactory.createForClass(Board);