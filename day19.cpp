#include <iostream>
#include <stdlib.h>

struct node {
  int id;
  int presents;
  struct node *next;
  

};

//int size=5;
int size=3004953;

int part1(struct node *first){

  while (first->next != first){
    
    //std::cout << "REMOVING: "<< first->next->id << std::endl;
    first->next = first->next->next;
    first = first->next;
  }
  return first->id;
}


int part2(struct node *first,int size){
  //  first = first->next;
  struct node *current,*t;
  int done=0;
  
  // set the stage by moving t half way down the ring
  current=first;
  t=first;
  while (!done){
    current=current->next->next;
    t=t->next;
    if (current==first or current->next == first)
      done=1;
  }


  /* now t is halfway */
  int step=0;
  while (first->next != first){
    
    /* remove halfway */
    t->next->prev  = t->prev;
    t->prev->next = t->next;


    first = first->next;
    t=t->next;
    
    step++;

    if (step%2!=0)
      t=t->next;
    
      
  }
  return first->id;
}





struct node *make_ring(int size){
  int i;
  struct node *n;
  struct node *current,*first;

  first = (struct node *)malloc(sizeof(struct node));
  first->id=1;
  current=first;
  
  for  (i=0;i<size-1;i++){
    n=(struct node *)malloc(sizeof(struct node));
    n->id=i+1;
    n->prev=current;
    current->next=n;
    current=n;
    
  }
  current->next=first;
  first->prev=current;
  return first;

}

int main(){
  struct node *first;

  first = make_ring(size);
  std::cout << part1(first)+1 << std::endl;
  free(first);
  first = make_ring(size);
  std::cout << part2(first,size)+1 << std::endl;
  free(first);
}
