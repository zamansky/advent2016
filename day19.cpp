#include <iostream>
#include <stdlib.h>
struct node {
  int id;
  int presents;
  struct node *next;
  struct node *prev;

};

//int size=5;
int size=3004953;

int part1(struct node *first){
  //  first = first->next;
  while (first->next != first){
    
    //std::cout << "REMOVING: "<< first->next->id << std::endl;
    first->next->next->prev = first;
    first->next = first->next->next;
    //    first->prev->next = first->next;
    //first->next->prev = first->prev;
    first = first->next;
    
      
  }
  return first->id;
}


int part2(struct node *first,int size){
  //  first = first->next;
  struct node *current,*t;
  int done=0;
  
  // stage
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

int zloopit(struct node *n){
  while (1){
    std::cout << n->id << std::endl;
    n=n->next;
  }
  return 0;  
}


int main(){
  int i;
  struct node *n;
  struct node *current,*first;


  current = (struct node *)malloc(sizeof(struct node));
  first->id=1;
  first->presents=1;
  first = current;
  
  for  (i=0;i<size-1;i++){
    n=(struct node *)malloc(sizeof(struct node));
    n->id=i+1;
    
    n->presents=1;
    n->prev=current;
    current->next=n;
    current=n;
    
  }
  current->next=first;
  first->prev=current;
  //    std::cout << part1(first)+1 << std::endl;
  std::cout << part2(first,size)+1 << std::endl;
}
