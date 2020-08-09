# Edit Armature

Edit mode with an armature active


## Transformations

The list of available transformations depend on the active armature.
The addon reads the active armature structure and tries to detect a known model (e.g. Mannequin or Mixamo).


### Unknown armature

By default (for a single bone in this example), no transformations will be available (thus, empty menu).

Edit mode -> Armature -> Chiro (UE4) -> ...

[![Edit armature empty Menu](img/feature/edit-armature/empty/menu.png)](img/feature/edit-armature/empty/menu.png)


[![Edit armature empty](img/feature/edit-armature/empty/scene.png)](img/feature/edit-armature/empty/scene.png)


---


### Mixamo armature

#### Skeleton conversion

Rename the bones to their Mannequin counterparts. Delete redundant leaf bones.

Edit mode -> Armature -> Chiro (UE4) -> "Mixamo --> Skeleton conversion"

[![Edit Mixamo armature Skeleton Conversion Menu](img/feature/edit-armature/mixamo/skeleton-conversion-menu.png)](img/feature/edit-armature/mixamo/skeleton-conversion-menu.png)

[![Edit Mixamo armature Skeleton Conversion Action](img/feature/edit-armature/mixamo/skeleton-conversion-action.gif)](img/feature/edit-armature/mixamo/skeleton-conversion-action.gif)


---


### Mannequin armature

#### Connect the bones with children

Leaving the bone heads in place, connects the tails to the children where it makes sense, to follow the Mannequin skeleton structure.

Edit mode -> Armature -> Chiro (UE4) -> "Mannequin --> Connect the bones with children"

[![Edit Mannequin armature Connect the bones with children Menu](img/feature/edit-armature/mannequin/connect-the-bones-with-children-menu.png)](img/feature/edit-armature/mannequin/connect-the-bones-with-children-menu.png)

[![Edit Mannequin armature Connect the bones with children Action](img/feature/edit-armature/mannequin/connect-the-bones-with-children-action.gif)](img/feature/edit-armature/mannequin/connect-the-bones-with-children-action.gif)



---

#### Snap clavicles to Mannequin position

Moves clavicle heads to positions simiral to Mannequin, calculated relatively to "spine_03" bone.

Edit mode -> Armature -> Chiro (UE4) -> "Mannequin --> Snap clavicles to Mannequin position"

[![Edit Mannequin armature Snap clavicles to Mannequin position Menu](img/feature/edit-armature/mannequin/snap-clavicles-to-mannequin-position-menu.png)](img/feature/edit-armature/mannequin/snap-clavicles-to-mannequin-position-menu.png)

[![Edit Mannequin armature Snap clavicles to Mannequin position Action](img/feature/edit-armature/mannequin/snap-clavicles-to-mannequin-position-action.gif)](img/feature/edit-armature/mannequin/snap-clavicles-to-mannequin-position-action.gif)


---

#### Make twist bones

Generates Mannequin twist bones. Calculates length and positions relatively to the parent bones.
Does nothing for existing twist bones.

Edit mode -> Armature -> Chiro (UE4) -> "Mannequin --> Make twist bones"

[![Edit Mannequin armature Make twist bones Menu](img/feature/edit-armature/mannequin/make-twist-bones-menu.png)](img/feature/edit-armature/mannequin/make-twist-bones-menu.png)

[![Edit Mannequin armature Make twist bones Action](img/feature/edit-armature/mannequin/make-twist-bones-action.gif)](img/feature/edit-armature/mannequin/make-twist-bones-action.gif)


---

#### Bone Roll T-Pose

Corrects the bone rolls to follow the Mannequin armature composition.
Assumes the Mesh is T-Pose.

**WARNING**: if your mesh is not in T-Pose, the rolls will not be correct

Edit mode -> Armature -> Chiro (UE4) -> "Mannequin --> Bone Roll T-Pose"

[![Edit Mannequin armature Make twist bones Menu](img/feature/edit-armature/mannequin/bone-roll-tpose-menu.png)](img/feature/edit-armature/mannequin/bone-roll-tpose-menu.png)

[![Edit Mannequin armature Make twist bones Action](img/feature/edit-armature/mannequin/bone-roll-tpose-action.gif)](img/feature/edit-armature/mannequin/bone-roll-tpose-action.gif)


---

#### Bone Roll A-Pose (Advanced)

Corrects the bone rolls to follow the Mannequin armature composition.
Assumes the Mesh is Mannequin A-Pose.

**WARNING**: if your mesh is not in A-Pose, the rolls will not be correct

---

#### Make IK bones (Advanced)

Generates IK bones for the armature.

Same as [Add Armature -> Mannequin IK Bones](add-armature.md#mannequin-ik-bones-advanced)

---

#### Chiropract on Armature (Advanced)

Corrects the bone arrangement so that it follows The Original Mannequin armature.
After this operation the character may be exported to FBX (with YX axis).
