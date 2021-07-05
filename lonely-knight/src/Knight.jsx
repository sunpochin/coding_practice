import { DragPreviewImage, useDrag } from 'react-dnd';
import { ItemTypes } from './ItemTypes';
// import { knightImage } from './knightImage';

import React from 'react'

export default function Knight() {
  const [{ isDragging }, drag] = useDrag(() => ({
    type: ItemTypes.KNIGHT,
    collect: (monitor) => ({
      isDragging: !!monitor.isDragging()
    })
  }))

  // return <span>♘</span>
  return (
    <div
      ref={drag}
      style={{
        // opacity: isDragging ? 0.5 : 1,
        fontSize: 25,
        fontWeight: 'bold',
        cursor: 'move',
      }}
    >
      ♘
    </div>
  )  
}
